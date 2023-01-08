#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Singly linked list
 * Return: 0 if there is no cycle, 1 is there is a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *tmp;

    if (!list)
    {
        return (0);
    }
    while (list)
    {
        tmp = list;
        list = list->next;
        if (tmp <= list)
        {
            return (1);
        }
    }
    return (0);
}
