#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: The linked list to be checked.
 *
 * Return: 1 if the list contains a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (!list)
        return (0);

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    }

    return (0);
}
