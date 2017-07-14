%image = imread('Glyph.png');
%template = image(75:165, 150:185);
im = imread('Image.png');
tpl = imread('Template.png');

image = im(:,:,1)
template = tpl(:,:,1)


imshowpair(image,template,'montage');


[y x] = find_corr(template, image);
disp([y x]); % should be the top-left corner of template in tablet

line([x x],[y y+size(template,1)], 'color', 'r')
line([x x+size(template,2)],[y y], 'color', 'r')
line([x+size(template,2) x+size(template,2)],[y y+size(template,1)], 'color', 'r')
line([x x+size(template,2)],[y+size(template,1) y+size(template,1)], 'color', 'r')











