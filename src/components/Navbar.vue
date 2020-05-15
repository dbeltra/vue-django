<template>
<nav class="menu" role="navigation" aria-label="main navigation">
  <p class="menu-label">
    General
  </p>
  <ul class="menu-list">
    <li><a>Home</a></li>
    <li><a>Section one</a></li>
  </ul>
  <p class="menu-label">
    User area
  </p>
  <ul class="menu-list">
    <li><a>My profile</a></li>
    <li><a>Shipping addresses</a></li>
  </ul>
</nav>
</template>


<script>


export default {
    name: 'Navbar',
    data() {
        return { 

        }
    },
};
</script>

<style>
.menu-label{
  padding-left: .7em
}

</style>
