<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'

  let message = '';
  let products: any[] = [];
  let newProduct = {
    name: '',
    description: '',
    price: 0,
    stock_quantity: 0,
    category_id: null,
    brand_id: null,
    is_active: true,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString()
  };

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

  async function addProduct() {
    const res = await fetch('/api/products', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newProduct)
    });
    if (res.ok) {
      await fetchProducts();
      message = 'Product added!';
      // Reset form
      newProduct = {
        name: '',
        description: '',
        price: 0,
        stock_quantity: 0,
        category_id: null,
        brand_id: null,
        is_active: true,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      };
    } else {
      message = 'Failed to add product';
    }
  }

  async function removeProduct(product_id: number) {
    const res = await fetch(`/api/products/${product_id}`, {
      method: 'DELETE'
    });
    if (res.ok) {
      await fetchProducts();
      message = 'Product removed!';
    } else {
      message = 'Failed to remove product';
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

  <h2>Add Product</h2>
  <form on:submit|preventDefault={addProduct}>
    <input placeholder="Name" bind:value={newProduct.name} required />
    <input placeholder="Description" bind:value={newProduct.description} />
    <input type="number" placeholder="Price" bind:value={newProduct.price} required />
    <input type="number" placeholder="Stock Quantity" bind:value={newProduct.stock_quantity} />
    <input type="number" placeholder="Category ID" bind:value={newProduct.category_id} />
    <input type="number" placeholder="Brand ID" bind:value={newProduct.brand_id} />
    <button type="submit">Add Product</button>
  </form>

  <h2>Products</h2>
  {#if products.length > 0}
    <ul>
      {#each products as product}
        <li>
          <strong>{product.name}</strong> - {product.description}
          <button on:click={() => removeProduct(product.product_id)}>Remove</button>
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