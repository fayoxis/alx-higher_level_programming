#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return NULL;
    new->n = number;
 /* If the list is empty or the number is smaller than the head, */
    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return new;
    }
 /* Find the appropriate position to insert the new node */
    while (node->next)
    {
        if (node->next->n >= number)
            break;
        node = node->next;
    }
 /* Insert the new node */
    new->next = node->next;
    node->next = new;

    return new;
}
