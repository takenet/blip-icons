<template>
  <div class="image-catalog">
    <h1>Desk SVG Files</h1>
    <div id="svg-browser" class="image-browser">
      <svg-container
        v-for="(svg, index) in $options.svgLibrary"
        v-once
        :key="index"
        :originalPath="svg.originalPath"
        :path="svg.path"/>
    </div>
  </div>
</template>

<script>
import { importAll } from '@/utils/functions';
import SvgContainer from './SvgContainer.vue';

const deskSvgFiles = importAll(require.context('../../assets/img/organized-new/desk/all', true, /\.svg$/));
const svgLibrary = [
  ...new Set(deskSvgFiles),
];

export default {
  name: 'new-desk-image-catalog',
  svgLibrary,
  components: {
    SvgContainer,
  },
};
</script>

<style>
</style>
