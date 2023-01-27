<script lang="ts">
	import ApiCalls from '$lib/ApiCalls.svelte';
import Chart from '$lib/Chart.svelte';
	import FanController from '$lib/FanController.svelte';
import Navbar from '$lib/Navbar.svelte';
	import PressureProbe from '$lib/PressureProbe.svelte';
	import TempProbe from '$lib/TempProbe.svelte';
</script>

<body>
	<Navbar />
    
    <div class="container">
        <div class="row">
          <div class="col-sm">
            <TempProbe />
          </div>
          <div class="col-sm">
            <PressureProbe />
          </div>
          <div class="col-sm">
            <ApiCalls />
          </div>
        </div>
        <div class="row">
            <div class="col-sm">
              <FanController />
            </div>
            <div class="col-sm">
              One of three columns
            </div>
            <div class="col-sm">
              One of three columns
            </div>
          </div>
          <div class="row">
            <div class="col-sm">
              <Chart />
            </div>
            <div class="col-sm">
              One of three columns
            </div>
            <div class="col-sm">
              One of three columns
            </div>
          </div>
      </div>
</body>

