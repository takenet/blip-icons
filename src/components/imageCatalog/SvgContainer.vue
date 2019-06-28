<template>
  <figure class="image-container svg-container">
    <div class="image-div" v-if="!isLogo">
      <img v-for="size in $options.sizes"
        :src="path"
        :alt="alt"
        :title="title"
        :key="size"
        :width="size"
        :height="size"/>
    </div>
    <img v-if="isLogo"
    :src="path"
    :alt="alt"
    :title="title"
    width="100%"/>
    <figcaption v-if="fileName">{{fileName}}</figcaption>
  </figure>
</template>

<script>
const sizes = [
  '72px',
  '40px',
  '32px',
  '24px',
  '20px',
  '16px',
  '14px',
  '12px',
  '10px',
];

export default {
  name: 'svg-container',
  sizes,
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
    isLogo() {
      return this.fileName.includes('-logo') || this.fileName.includes('logo-');
    },
  },
};
</script>

<style>
.image-div {
  width: 100%;
  height: 100%;
}
</style>
