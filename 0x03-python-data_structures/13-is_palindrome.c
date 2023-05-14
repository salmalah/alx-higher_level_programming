#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - A fucntion check if linked list is a palindrome
 * @head: the head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *p = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (f && (*f).next)
	{
		f = (*(*f).next).next;
		temp = s;
		s = (*s).next;
		(*temp).next = p;
		p = temp;
	}
	if (f)
		s = (*s).next;
	while (s && p)
	{
		if ((*s).n != (*p).n)
			return (0);
		s = (*s).next;
		p = (*p).next;
	}
	return (1);
}

