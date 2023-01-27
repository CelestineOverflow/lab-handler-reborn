<script lang="ts">
    import 'bootstrap/dist/css/bootstrap.min.css';
    import 'bootstrap-icons/font/bootstrap-icons.css';
</script>

<nav class="navbar">
    <a class="navbar-brand" href="/">
        <img src="/icon.png" alt="" width="42" height="42" class="d-inline-block align-text-top">
        <span class="navbar-text">Lab Handler <span class="badge bg-success">Alpha!</span></span>
    </a>
    <form class="form-inline">
        <button class="btn btn-outline-success" type="button">Enable <i class="bi bi-stop-circle"></i></button>
        <button class="btn btn-outline-danger" type="button">Stop <i class="bi bi-stop-circle"></i></button>
        <a class="navbar-brand" href="/help">Help <i class="bi bi-question-circle"></i></a>
        <a class="navbar-brand" href="/about">Docs <i class="bi bi-book"></i></a>
        <a class="navbar-brand" href="/config">Config <i class="bi bi-gear"></i></a>
        <a class="navbar-brand" href="/manual_control">Manual Control <i class="bi bi-joystick"></i></a>
    </form>
</nav>