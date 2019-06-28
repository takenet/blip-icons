<template>
  <div class="image-catalog">
    <div id="svg-browser">
      <p>SVG files</p>
      <div id="svg-browser" class="image-browser">
        <svg-container
          v-for="(svg, index) in svgs"
          v-once
          :key="index"
          :originalPath="svg.originalPath"
          :path="svg.path"/>
      </div>
    </div>

    <div id="png-browser">
      <p>PNG files</p>
      <div id="png-browser" class="image-browser">
        <image-container
          v-once
          v-for="(png, index) in pngs"
          :key="index"
          :originalPath="png.originalPath"
          :path="png.path"/>
      </div>
    </div>

  </div>
</template>

<script>
import ImageContainer from './ImageContainer.vue';
import SvgContainer from './SvgContainer.vue';

function importAll(files) {
  const keys = files.keys();
  const pathMap = keys.map(files);
  return keys.map(
    (key, index) => {
      const path = pathMap[index];
      return {
        originalPath: key,
        path,
      };
    },
  );
}

const svgFiles = importAll(require.context('../../assets/img/organized-old', true, /\.svg$/));
const pngFiles = importAll(require.context('../../assets/img/organized-old', true, /\.png$/));

export default {
  name: 'old-image-catalog',
  components: {
    ImageContainer,
    SvgContainer,
  },
  data() {
    return {
      pngArray: pngFiles,
      svgArray: svgFiles,
    };
  },
  computed: {
    svgs() {
      return [...new Set(this.svgArray)];
    },
    pngs() {
      return this.pngArray;
    },
  },
};
</script>

<style>
</style>
