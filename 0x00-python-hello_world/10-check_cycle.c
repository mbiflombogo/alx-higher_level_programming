#include "lists.h"
/**
  * check_cycle - check if list has a cycle
  * @list: var of type listint_t
  * Return: 0 if no cycle, 1 if cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *tort = list, *hare = list;

	while (tort != NULL && hare != NULL && hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
			return (1);
	}
	return (0);
}
