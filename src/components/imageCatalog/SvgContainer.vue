<template>
  <figure class="image-container svg-container">
    <img :src="path" :alt="alt" :title="title"/>
    <figcaption v-if="fileName">{{fileName}}</figcaption>
  </figure>
</template>

<script>
export default {
  name: 'svg-container',
  props: {
    originalPath: {
      type: String,
    },
    path: {
      type: String,
      required: true,
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
svg {
  display: block;
  width: 120px;
  height: 120px;
}
</style>
