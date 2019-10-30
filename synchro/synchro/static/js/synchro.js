/*
<!-- Menu Toggle Script -->
<script>
$("#menu-toggle").click(function(e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});
</script>
*/

/* Open the sidenav */
function openNav() {
    document.getElementById("mySidenav").style.width = "100%";
  }
  
  /* Close/hide the sidenav */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  } 


$(document).ready(function(){
    // Initializes tooltips
    $('[title]').tooltip({container: 'body'});

    //Apply img-thumbnail class to body-content images
    $('.body-content img').addClass("img-thumbnail");
});