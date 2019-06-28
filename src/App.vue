<template>
  <div id="app">
    <div class="wrapper">
      <nav>
        <ul>
          <li>
            <a @click="changeTab($options.CatalogTabs.Portal)">
              {{ $options.CatalogTabs.Portal }}
            </a>
          </li>

          <li>
            <a @click="changeTab($options.CatalogTabs.Desk)">
              {{ $options.CatalogTabs.Desk }}
            </a>
          </li>

          <li>
            <a @click="changeTab($options.CatalogTabs.Old)">
              {{ $options.CatalogTabs.Old }}
            </a>
          </li>
        </ul>
      </nav>
      <new-portal-image-catalog
        class="new-catalog"
        v-show="currentTab === $options.CatalogTabs.Portal">
      </new-portal-image-catalog>

      <new-desk-image-catalog
        class="new-catalog"
        v-show="currentTab === $options.CatalogTabs.Desk">
      </new-desk-image-catalog>

      <old-image-catalog
        class="old-catalog"
        v-show="currentTab === $options.CatalogTabs.Old">
      </old-image-catalog>
    </div>
  </div>
</template>

<script>
import OldImageCatalog from './components/imageCatalog/OldImageCatalog.vue';
import NewPortalImageCatalog from './components/imageCatalog/NewPortalImageCatalog.vue';
import NewDeskImageCatalog from './components/imageCatalog/NewDeskImageCatalog.vue';

const CatalogTabs = {
  Portal: 'Portal',
  Desk: 'Desk',
  Old: 'Old',
};

export default {
  name: 'app',
  CatalogTabs,
  components: {
    OldImageCatalog,
    NewPortalImageCatalog,
    NewDeskImageCatalog,
  },
  data() {
    return {
      currentTab: CatalogTabs.Portal,
    };
  },
  methods: {
    changeTab(tab) {
      this.currentTab = tab;
    },
  },
};
</script>

<style>
body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  background: #E3FFAA;
  color: #52636c;
  text-align: center;
}

.wrapper {
  padding: 40px;
}

nav ul {
  list-style: none;
  display: block;
  width: 100%;
  text-align: center;

    margin-block-start: 0;
    margin-block-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    padding-inline-start: 0;
}

nav ul li {
  display: inline;
  margin-right: 20px;
}

nav ul li:last-child {
  margin-right: 0;
}

nav ul li a {
  cursor: pointer;
  font-weight: 600;
}

nav ul li a:hover {
  color: #0cc8cc;
}

.image-container {
  position: relative;
  width: 120px;
  min-height: 120px;
  padding: 15px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 2px solid #0cc8cc;
  border-radius: 10px;
}

.image-container figcaption {
  position: absolute;
  left: 0;
  bottom: 0;
  display: block;
  width: 100%;
  text-align: center;
  background-color: #0cc8cc;
  font-size: 14px;
}

.image-container img {
  display: inline-block;
}

.image-browser {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
