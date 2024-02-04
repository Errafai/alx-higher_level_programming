#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL) return NULL;
	if ((*head)->n > number || *head == NULL)
	{
		new->n = number;
		new->next = *head;
		*head = new;
	}
	else
	{
		curr = *head;
		while (curr->next->n < number)
		{
			curr = curr->next;
			if (curr == NULL)
			{
				free(new);
				return add_nodeint_end(head, number);
			}
		}
		new->n = number;
		temp = curr->next;
		curr->next = new;
		new->next = temp;
	}
	return (new);
}
