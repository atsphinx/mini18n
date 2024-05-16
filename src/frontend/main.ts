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
  /**
   * Handler for changing value of selectbox.
   */
  export const redirectBySelect = (e: Event) => {
    if (!(e.target instanceof HTMLSelectElement)) {
      console.error("This handler should be called only from <select>");
      return;
    }
    const langCode = e.target.value;
    const langUrl = e.target.selectedOptions[0].dataset.url ?? false;
    if (langCode && langUrl) {
      redirectWithRemember(langCode, langUrl);
    }
    console.error("Target URL is not found.");
  };
}

console.debug(`Current version is ${packageJson.version}`);
