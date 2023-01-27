<script lang="ts">
    import 'bootstrap/dist/css/bootstrap.min.css';
    import 'bootstrap-icons/font/bootstrap-icons.css';
	import Navbar from '$lib/Navbar.svelte';
	import Dpad from '$lib/Dpad.svelte';
	import Tray from '$lib/Tray.svelte';
</script>
<Navbar />

<div class="container">
	<div class="row">
	  <div class="col-sm">
		<Tray />
	  </div>
	  <div class="col-sm">
		One of three columns
	  </div>
	  <div class="col-sm">
		<Dpad />
	  </div>
	</div>
  </div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
</style>