#include "lists.h"


/**
* add_nodelong3 - ENTRYPOINT
* @head : constant
* @n: int
* Return: 0 success or uint
*/

store_addr *add_nodelong3(store_addr **head, const unsigned long n)
{

	store_addr *node = malloc(sizeof(store_addr));

	if (node)
	{
		node->p = n;
		node->next = *head;
		*head = node;
	}
	if (*head)
		return (*head);
	return (NULL);
}

/**
* get_nodelong3- ENTRYPOINT
* @head : listint_t type
* @value: int unsgned
* Return: 0 success or uint
*/
int get_nodelong3(store_addr *head, unsigned long value)
{
	store_addr *node = head;

	if (!node)
	{
		return (0);
	}
	while (node)
	{
		if (node->p == value)
		{
			return (1);
		}
		node = node->next;
	}
	return (0);
}

/**
* free_listlong3 - ENTRYPOINT
* @head : constant
* Return: 0 success or uint
*/

void free_listlong3(store_addr *head)
{

	store_addr *tmp;

	if (!head)
		return;
	while (head)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
	if (tmp)
		free(tmp);
}
/**
* check_cycle - ENTRYPOINT
* @list: 1 param
* Return: 0 success or uint
*/

int check_cycle(listint_t *list)
{
	listint_t *store = list, *tmp = NULL;
	store_addr *hd = NULL;
	size_t true = 0;

	if (list == NULL)
	{
		return (true);
	}
	while (store != NULL)
	{
		tmp = store;
		store = store->next;
		add_nodelong3(&hd, (unsigned long) tmp);
		true = get_nodelong3(hd, (unsigned long)store);
		if (true)
		{
			free_listlong3(hd);
			return (true);
		}
	}
	free_listlong3(hd);
	return (true);
}
