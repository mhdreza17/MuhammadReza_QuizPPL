<?php
require('koneksi.php');
session_start();

// Jika belum login, redirect ke login
if( !isset($_SESSION['username']) ) {
    header('Location: login.php');
    exit;
}

$username = $_SESSION['username'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <title>Quiz Pengupil - Dashboard</title>
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <h2 class="text-center mb-4">Selamat Datang, <?= htmlspecialchars($username); ?>!</h2>
                
                <div class="card">
                    <div class="card-body">
                        <p class="card-text">Ini adalah halaman dashboard Quiz Pengupil.</p>
                        <p class="card-text">Anda telah berhasil login.</p>
                    </div>
                </div>

                <div class="mt-4 text-center">
                    <a href="logout.php" class="btn btn-danger">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html>
