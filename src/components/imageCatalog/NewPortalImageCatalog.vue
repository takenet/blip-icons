<template>
  <div class="image-catalog">
    <h1>Portal SVG Files</h1>
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

const portalSvgFiles = importAll(require.context('../../assets/img/organized-new/portal/all', true, /\.svg$/));
const svgLibrary = [
  ...new Set(portalSvgFiles),
];

export default {
  name: 'new-portal-image-catalog',
  svgLibrary,
  components: {
    SvgContainer,
  },
};
</script>

<style>
</style>
