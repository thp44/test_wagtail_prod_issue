//  Chat - Initializes the autosize library and scrolls chat list to bottom

/* global autosize */
import mrUtil from './util';

autosize(document.querySelectorAll('.chat-module-bottom textarea'));

// Scrolls the chat-module-body to the bottom
(($) => {
  $(window).on('load', () => {
    const lastChatItems = document.querySelectorAll('.media.chat-item:last-child');
    if (lastChatItems) {
      mrUtil.forEach(lastChatItems, (index, item) => {
        item.scrollIntoView();
      });
    }
  });
})(jQuery);
