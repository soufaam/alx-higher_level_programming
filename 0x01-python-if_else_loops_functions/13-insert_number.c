#include "lists.h"
#include <stdio.h>

/**
* insert_node - ENTRYPOINT
* @head : first param
* @number : 2 parama
* Return: 0 success or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *node = malloc(sizeof(listint_t)), *ntmp = *head, *tmpnode = NULL;

	if (node)
		node->n = number;
	else
		return (NULL);
	if (!ntmp || !head)
	{
		*head = node;
		return (*head);
	}
	if (node->n < ntmp->n)
	{
		node->next = ntmp;
		*head = node;
		return (*head);
	}
	tmpnode = ntmp;
	while (ntmp)
	{
		if (node->n < ntmp->n)
		{
			node->next = ntmp;
			tmpnode->next = node;
			return(tmpnode);
		}
		else if (ntmp->next == NULL)
		{
			ntmp->next = node;
			node->next = NULL;
			return (*head);
		}
		tmpnode = ntmp;
		ntmp = ntmp->next;
	}
	return (*head);
}
