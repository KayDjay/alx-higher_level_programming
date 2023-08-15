#include "lists.h"
/**
 * is_palindrome - Function that checks if the palindrome list is singly list
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int list[100];
	int a, b;

	listint_t *p = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	a = 0;
	while (p)
	{
		list[a] = p->n;
		p = p->next;
		a++;
	}
	a = a - 1;

	for (b = 0; a > b; a--, b++)
	{
		if (list[b] != list[a])
			return (0);
	}

	return (1);
}
