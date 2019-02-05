//Error timeout
setTimeout(error, 5000);

function error() {
  $("#error").fadeOut().empty();
}

//Password timeout
setTimeout(fade_out, 0);

function fade_out() {
  $("#id_password").hide().empty();
}

//Responsive table
$(document).ready(function() {
    $('#dataTables-example').DataTable({
        responsive: true
    });
});
