function [yIndex,xIndex] = find_corr(template, img)

c = normxcorr2(template, img);
[ypeak, xpeak] = find(c==max(c(:)));
yIndex=ypeak-size(template,1)+1;
xIndex=xpeak-size(template,2)+1; 

end