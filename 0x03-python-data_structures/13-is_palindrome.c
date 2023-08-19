#include "lists.h"

/**
 * add_nodeint - frees a listint_t list
 * @head: pointer to list to be freed
 * @n: number
 * Return: void
 */
listint_t *add_nodeint (listint_t **head, const int n)
{

	listint_t *node = malloc(sizeof(listint_t));

	if (node)
	{
		node->n = n;
		node->next = *head;
		*head = node;
	}
	if (*head)
		return (*head);
	return (NULL);
}

/**
 * reverse_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
listint_t *reverse_listint(listint_t *head)
{
	listint_t *h = NULL;
	listint_t *tmp = head;

	while (tmp)
	{
		add_nodeint(&h, tmp->n);
		tmp = tmp->next;
	}
	printf("here");
	return (h);
}

/**
 * is_palindrome - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;
	listint_t *tmp = *head;
	int check = 0;

	reversed = reverse_listint(tmp);
	while (tmp && reversed)
	{
		if (tmp->n == reversed->n)
			check = 1;
		else
		{
			check = 0;
			break;
		}
		tmp = tmp->next;
		reversed = reversed->next;
	}
	return (check);
}
