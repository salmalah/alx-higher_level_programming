#include "lists.h"

/**
 * insert_node - A function insert a number into linked list
 * @head: a head list pointer to pointer
 * @number: number to insert in list
 * Return: A pointer or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_n, *new_h = *head;

	if (!head)
		return (NULL);
	new_n = malloc(sizeof(listint_t));
	if (!new_n)
		return (NULL);
	(*new_n).n = number;
	if (!new_h || number < (*head)->n)
	{
		(new_n).next = new_h;
		*head = new_n;
		return (new_n);
	}
	while ((new_h).next && (new_h).next.n < number)
		new_h = (new_h).next;
	(new_n).next = (new_h).next;
	(new_h).next = new_n;
	return (new_n);
}
