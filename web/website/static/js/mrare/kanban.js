// Kanban - Initializes the Shopify Draggable library on our Kanban elements.

/* global Draggable, SwapAnimation */
/* eslint-disable no-unused-vars */

const mrKanban = {
  sortableKanbanLists: new Draggable.Sortable(document.querySelectorAll('div.kanban-board'), {
    draggable: '.kanban-col:not(:last-child)',
    handle: '.card-list-header',
  }),

  sortableKanbanCards: new Draggable.Sortable(document.querySelectorAll('.kanban-col .card-list-body'), {
    plugins: [SwapAnimation.default],
    draggable: '.card-kanban',
    handle: '.card-kanban',
    appendTo: 'body',
  }),
};
