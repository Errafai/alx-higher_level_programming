#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL) return NULL;
	new->n = number;
	if ((*head)->n > number || *head == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		curr = *head;
		while (curr->next->n < number)
			curr = curr->next;
		temp = curr->next;
		curr->next = new;
		new->next = temp;
	}
	return (new);
}
