#include "lists.h"
#include<string.h>
/**
  * is_palindrome - check list if palindr
  * @head: first node
  * Return: 0 - !palindr, else 1
  */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_palind(head, *head));
}
/**
  * is_palind - check if palindrome
  * @head: first node
  * @end: last node
  * Return: 0, or 1
  */
int is_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (is_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
