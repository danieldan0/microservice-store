<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'

  let message = '';
  let products: any[] = [];

  async function fetchHealth() {
    const res = await fetch('/api/health');
    message = await res.text();
  }

  async function fetchProducts() {
    const res = await fetch('/api/products');
    if (res.ok) {
      products = await res.json();
    } else {
      products = [];
    }
  }

  fetchProducts();
</script>

<main>
  <div>
    <a href="https://vite.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <button on:click={fetchHealth}>Check API Health</button>
  <p>{message}</p>

  <div class="card">
    <Counter />
  </div>

  <h2>Products</h2>
  {#if products.length > 0}
    <ul>
      {#each products as product}
        <li>
          <strong>{product.name}</strong> - {product.description}
        </li>
      {/each}
    </ul>
  {:else}
    <p>No products found.</p>
  {/if}

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
