#include "lists.h"
#include <stdlib.h>
/**
  * insert_node - inserts no. in sorted list
  * @head: first node
  * @number: no. to be inserted
  *
  * Return: type listint_t
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
