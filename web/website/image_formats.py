from wagtail.images.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
unregister_image_format('left')
unregister_image_format('right')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image img-responsive full-width', 'width-400'))
register_image_format(Format('left', 'Left-aligned', 'richtext-image img-responsive left', 'width-200'))
register_image_format(Format('right', 'Right-aligned', 'richtext-image img-responsive right', 'width-200'))
