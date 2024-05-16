/**
 * Module to manage cross-move into i18n sites.
 */
import Cookies from "js-cookie";
import * as packageJson from "../../package.json";

const COOKIE_SELECTED_LANG = "lang";
const COOKIE_MAX_AGE_DAYS = 400;

/**
 * Redirect page of selected language.
 */
const redirectWithRemember = (lang: string, url: string) => {
  Cookies.set(COOKIE_SELECTED_LANG, lang, {
    sameSite: "strict",
    path: "/",
    expires: new Date(
      new Date().getTime() + 1000 * 60 * 60 * 24 * COOKIE_MAX_AGE_DAYS,
    ),
  });
  location.href = url;
};

/**
 * Handlers for HTML
 */
export namespace Widget {
  export const redirectBySelect = (e: Event) => {
    //
    const langCode = e.target.value;
    const langUrl = e.target.selectedOptions[0].dataset.url;
    redirectWithRemember(langCode, langUrl);
  };
}

console.debug(`Current version is ${packageJson.version}`);
