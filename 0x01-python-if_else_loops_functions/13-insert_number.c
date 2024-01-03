#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current = *head, *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;
    new_node->n = number;

    /* If the list is empty or the number is smaller than the head,*/
    if (current == NULL || current->n >= number)
    {
        new_node->next = current;
        *head = new_node;
        return new_node;
    }

    /* Find the appropriate position to insert the new node */
    while (current->next && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}
