const divElement = document.querySelector('#directory');

divElement.addEventListener('scroll', () => {
  localStorage.setItem('scrollPosition', divElement.scrollTop);
});
document.addEventListener('DOMContentLoaded', () => {
  const scrollPosition = localStorage.getItem('scrollPosition');
  if (scrollPosition) {
    divElement.scrollTop = scrollPosition;
  }
});

window.addEventListener('scroll', () => {
  localStorage.setItem('scrollWindowPosition', window.scrollY);
});

document.addEventListener('DOMContentLoaded', () => {
  const scrollPosition = localStorage.getItem('scrollWindowPosition');
  if (scrollPosition) {
    window.scrollTo(0, scrollPosition);
  }
});