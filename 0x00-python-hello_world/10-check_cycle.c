#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: The linked list to be checked.
 *
 * Return: 1 if the list contains a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *current = list;
    listint_t *runner = list;

    while (current && runner && runner->next)
    {
        current = current->next;
        runner = runner->next->next;

        if (current == runner)
            return 1;
    }

    return 0;
}
