//
// Created by Diego Magdaleno on 10/5/20.
//
/* Internal headers part of the
 * default C++ lib */
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
#include <chrono>

/* Third party and external resources */
#include <nlohmann/json.hpp>

class PackageNode {
private:
    std::string nodeName;
    std::vector<PackageNode*> edges; // Our package dependencies

public:
    PackageNode(std::string name) : nodeName(name) { }

    void addEdge(PackageNode *node) {
        edges.push_back(node);
    }

    std::string getName() {
        return nodeName;
    }

    const std::vector<PackageNode*> &getEdges() const {
        return edges;
    }
};

void depResolve(PackageNode *node, std::vector<PackageNode*> *resolved, std::vector<PackageNode*> *seen) {
    seen->push_back(node);
    for (auto& edge : node->getEdges()) {
        if (std::find(resolved->begin(), resolved->end(), edge) == resolved->end()) {
            depResolve(edge, resolved, seen);
        }
    }
    resolved->push_back(node);
}

std::map<std::string, PackageNode*> packageNodeDict;

void fileToDict(std::string path) {
    std::ifstream ifs(path);

    nlohmann::json jsonMap = nlohmann::json::parse(ifs);

    for (auto& depDict : jsonMap) {
        packageNodeDict.insert(std::make_pair(depDict["name"], new PackageNode(depDict["name"])));
    }

    /* Second round
     * now we insert the dependencies, this is
     * harder since we are using pointers
     * time to play with memory
     */
    for (auto& depDict: jsonMap) {
        if(depDict.find("depends") != depDict.end()) {
            for (auto& eachDep: depDict["depends"]){
                packageNodeDict[depDict["name"]]->addEdge(packageNodeDict[eachDep]);
            }
        }
    }
}

int main() {

    std::vector<PackageNode*> solvedTest;
    std::vector<PackageNode*> seenTest;

    fileToDict("/Users/me/Documents/Projects/Vodka/dep.json");
    std::string name;

    std::cout << "For what package of the tree you want to resolve deps?: ";
    std::cin >> name;

    auto start = std::chrono::steady_clock::now();

    depResolve(packageNodeDict[name], &solvedTest, &seenTest);
    for (int i = 0; i < solvedTest.size(); i++) {
        std::cout << solvedTest[i]->getName() << std::endl;
    }

    auto end = std::chrono::steady_clock::now();
    auto diff = end - start;


    std::cout << "Resolved tree, took: " << std::chrono::duration <float> (diff).count() << " seconds" << std::endl;

    return 0;
}

