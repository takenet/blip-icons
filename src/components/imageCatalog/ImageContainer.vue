<template>
  <figure class="image-container png-container">
    <img :src="path" :alt="alt" :title="title"/>
    <figcaption v-if="fileName">{{fileName}}</figcaption>
  </figure>
</template>

<script>
export default {
  name: 'image-container',
  props: {
    originalPath: {
      type: String,
    },
    path: {
      type: String,
    },
    alt: {
      type: String,
      default: 'Image',
    },
    title: {
      type: String,
      default: 'Image',
    },
  },
  computed: {
    fileName() {
      if (!this.originalPath) {
        return undefined;
      }
      const splitPath = this.originalPath.split('/');
      const fileName = splitPath[splitPath.length - 1].split('.')[0];
      return fileName;
    },
  },
};
</script>

<style>
img {
  display: block;
}

#png-browser img {
  max-width: 120px;
  max-height: 120px;
}

#svg-browser img {
  width: 120px;
  height: 120px;
}
</style>
