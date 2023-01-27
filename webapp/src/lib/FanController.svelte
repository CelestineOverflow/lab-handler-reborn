<script lang="ts">
    let fanSpeed: number = 0;
</script>

//fan icon 
<i class="bi bi-fan"></i>

<div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Fan Controll<i class="bi bi-telephone"></i></h5>
      <i class="bi bi-fan"></i>
      <slider min={0} max={100} step={1} />
    </div>
  </div>