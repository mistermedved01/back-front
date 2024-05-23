<template>
    <NConfigProvider :theme="darkTheme">
        <NLayout :native-scrollbar="false" position="absolute" :content-style="{ height: '100%' }">
            <NSpace justify="center" vertical align="center" :style="{ height: '100%' }">
                <NH1>
                    <NGradientText :type="env ? 'success' : 'error'"
                        >VITE_ENV: {{ env ? env : "Пустовато.." }}</NGradientText
                    >
                </NH1>
                <NH1>
                    <NGradientText :type="apiUrl ? 'success' : 'error'">
                        VITE_API_URL:
                        {{
                            apiUrl
                                ? apiUrl
                                : "Нет url до API :(((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))"
                        }}
                    </NGradientText>
                </NH1>
                <NH3 v-if="result" style="margin-top: 40px">
                    <NGradientText
                        gradient="linear-gradient(90deg, red 0%, green 50%, blue 100%)"
                        style="white-space: break-spaces"
                    >
                        {{ result }}
                    </NGradientText>
                </NH3>
                <NResult v-else status="404"> </NResult>
            </NSpace>
        </NLayout>
    </NConfigProvider>
</template>

<script lang="ts" setup>
import { NConfigProvider, NLayout, NGradientText, darkTheme, NSpace, NH1, NH3, NResult } from "naive-ui";

const env = import.meta.env.VITE_ENV;
const apiUrl = import.meta.env.VITE_API_URL;

const { data } = useAsyncData("songs", () => $fetch(apiUrl as string));

const result = computed(() => {
    if (data.value) {
        return JSON.stringify(data.value, null, 4);
    }

    return "";
});
</script>
