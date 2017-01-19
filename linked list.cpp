#include<stdlib.h>
#include<stdio.h>

struct Node {
  int data;
  Node* prev;
  Node* next;
};

Node* head;
Node* tail;

Node* createNewNode(int value) {

  Node* newNode = new Node();
  newNode -> data = value;
  newNode -> prev = NULL;
  newNode -> next = NULL;
  return newNode;

}

void InsertAtHead(int value) {

  Node* newNode = createNewNode(value);

  if (head == NULL) {
    head = newNode;
    return;
  }

  head -> prev = newNode;
  newNode -> next = head;
  head = newNode;

}

void Print() {
  Node* temp = head;

  while (temp != NULL) {
    printf("%d ", temp -> data);
    temp = temp -> next;
  }
  printf("\n");
}

void reversePrint() {

  Node* temp = head;
  if (temp == NULL) {
    return;
  }

  while (temp -> next != NULL) {
    temp = temp -> next;
  }

  while(temp != NULL) {
    printf("%d ", temp -> data);
    temp = temp -> prev;
  }

  printf("\n");

}

int main() {

  head = NULL;
  InsertAtHead(2); Print(); reversePrint();
  InsertAtHead(3); Print(); reversePrint();

}
