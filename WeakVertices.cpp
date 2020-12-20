#include <iostream>
#include <vector>
using namespace std;

void createGraph(vector<vector<int> >& graph, int rowLength, vector<bool>& weakPoints);
void findWeakPoints(vector<vector<int> >& graph, int rowLength, vector<bool>& weakPoints);
bool checkTriangle(int originalRow, int currentRow, int length, vector<bool>& weakPoints, vector<vector <int> >& graph);
void printWeakPoints(vector<bool>& weakPoints);

int main()
{
  vector<vector<int> > currentGraph;
  vector<bool> weakPoints;
  int graphSize;

  while(true)
  {
    currentGraph.clear();
    weakPoints.clear();
    cin >> graphSize;

    if(graphSize == -1)
      break;

    createGraph(currentGraph, graphSize, weakPoints);
    findWeakPoints(currentGraph, graphSize, weakPoints);
    printWeakPoints(weakPoints);

  }

  return 0;
}

void createGraph(vector<vector<int> >& graph, int rowLength, vector<bool>& weakPoints)
{
  vector<int> placeholder;
  int currentNum;

  for(int i = 0; i < rowLength; i++)
  {
    graph.push_back(placeholder);
    weakPoints.push_back(false);

    for(int y = 0; y < rowLength; y++)
    {
      cin >> currentNum;
      graph[i].push_back(currentNum);
    }
  }
}

void findWeakPoints(vector<vector<int> >& graph, int rowLength, vector<bool>& weakPoints)
{
  bool isWeak;
  for(int rowVal = 0; rowVal < rowLength; rowVal++)
  {
    if(weakPoints[rowVal])
      continue;

    isWeak = true;
    for(int colVal = 0; colVal < rowLength; colVal++)
    {
      if(graph[rowVal][colVal] == 1)
      {
        isWeak = checkTriangle(rowVal, colVal, rowLength, weakPoints, graph);
        if(!isWeak)
          break;
      }
    }
  }
}

bool checkTriangle(int originalRow, int currentRow, int length, vector<bool>& weakPoints, vector<vector <int> >& graph)
{
  for(int i = 0; i < length; i++)
  {
    if(graph[currentRow][i] == 1 && graph[originalRow][i] == 1)
    {
      weakPoints[originalRow] = true;
      weakPoints[currentRow] = true;
      return false;
    }
  }

  return true;
}

void printWeakPoints(vector<bool>& weakPoints)
{
  for(int i = 0; i < weakPoints.size(); i++)
  {
    if(!weakPoints[i])
      cout << i << " ";
  }

  cout << endl;
}
