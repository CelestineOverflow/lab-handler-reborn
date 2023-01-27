<script lang="ts">
    let x = 0;
    let y = 0;
    let z = 0;
</script>

<div class="card" style="width: 18rem;">
    <div class="card-body">
        <h6 class="card-subtitle mb-2 text-muted text-center">Manual Control</h6>
        <div class="container">
            <div class="row">
              <div class="col-sm">
                <button type="button" class="btn btn-outline-primary">Pick</button>
              </div>
              <div class="col-sm">
                <button type="button" class="btn btn-outline-primary">Y+</button>
              </div>
              <div class="col-sm">
                <button type="button" class="btn btn-outline-primary">Z+</button>
              </div>
            </div>
            <div class="row">
                <div class="col-sm">
                  <button type="button" class="btn btn-outline-primary">X-</button>
                </div>
                <div class="col-sm">
                  <button type="button" class="btn btn-outline-primary"><i class="bi bi-house"></i></button>
                </div>
                <div class="col-sm">
                  <button type="button" class="btn btn-outline-primary">X+</button>
                </div>
              </div>
                <div class="row">
                    <div class="col-sm">
                    <button type="button" class="btn btn-outline-primary">Place</button>
                    </div>
                    <div class="col-sm">
                    <button type="button" class="btn btn-outline-primary">Y-</button>
                    </div>
                    <div class="col-sm">
                    <button type="button" class="btn btn-outline-primary">Z-</button>
                    </div>
                </div>
                <div class="row">
                    <button type="button" class="btn btn-outline-secondary">Go to Socket</button>
                    <p class="card-text text-center">Current Position X: {x} Y: {y} Z: {z}</p>
                    <button type="button" class="btn btn-outline-warning">Set as Socket</button>
                </div>
          </div>
    </div>
  </div>