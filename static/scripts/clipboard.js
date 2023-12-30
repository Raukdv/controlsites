function myClipboardUsername() {
  let text = document.getElementById('myUsername').innerHTML;
  try {
      navigator.clipboard.writeText(text);

      //Pop up button message password
      // var popup = document.getElementById("myPopupUsername");
      // popup.classList.toggle("show");

      console.log('Content copied to clipboard');

    } catch (err) {
      console.error('Failed to copy: ', err);
    }
}

function myClipboardPassword() {
  let text = document.getElementById('myPassword').innerHTML;
  try {
      navigator.clipboard.writeText(text);

      //Pop up button message password
      // var popup = document.getElementById("myPopupPassword");
      // popup.classList.toggle("show");

      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
}
