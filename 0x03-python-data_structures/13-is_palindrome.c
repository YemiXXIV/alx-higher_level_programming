#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *second_half = reverse_list(slow);
	listint_t *first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(second_half);

			return (0);
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}

	reverse_list(second_half);

	return (1);
}
