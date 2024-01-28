#include "lists.h"
/**
 * check_cycle - check if there is a cycle in the list
 * @list: the head of the list
 * Return: 1 if these is a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
