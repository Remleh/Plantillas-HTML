document.getElementById('logoutButton').addEventListener('click', function () {
    Swal.fire({
        title: 'Are you sure?',
        text: "You are leaving the page",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, logout!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/logout/';
        }
    })
});