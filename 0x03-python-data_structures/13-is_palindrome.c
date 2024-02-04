#include "lists.h"

size_t len_list(listint_t *head)
{
	size_t i = 0;

	while (head)
	{
		head = head->next;
		i++;
	}
	return (i);
}

int is_palindrome(listint_t **head)
{
	size_t i = len_list(*head);
	int *array = malloc(sizeof(int) * i);
	size_t j = 0;

	if (array == NULL || *head==NULL)
		return (1);
	while (*head)
	{
		array[j] = (*head)->n;
		*head = (*head)->next;
		j++;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (array[j] != array[i - 1 - j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
