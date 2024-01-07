#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

int isPalindrome(Node* head) {
    Node* slow = head;
    Node* fast = head;
    Node* prev = NULL;

    /* Traverse the list and reverse the first half */
    while (fast && fast->next) {
        fast = fast->next->next;
        Node* temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* If the list has an odd number of elements, move slow pointer one step forward */
    if (fast)
        slow = slow->next;

    /* Compare the reversed first half with the second half */
    while (prev) {
        if (prev->data != slow->data)
            return 0;
        prev = prev->next;
        slow = slow->next;
    }

    return 1; /* The list is a palindrome */
}

Node* newNode(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

void freeList(Node* head) {
    Node* temp;
    while (head) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    Node* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(2);
    head->next->next->next->next = newNode(1);

    int result = isPalindrome(head);

    if (result)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    freeList(head);

    return 0;
}
