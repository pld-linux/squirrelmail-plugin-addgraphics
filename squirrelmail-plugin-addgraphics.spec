%define		_plugin	addgraphics
%define		mversion	1.0.3
Summary:	Plugin to allow custom graphic on the left-hand pane
Summary(pl):	Wtyczka umo¿liwiaj±ca dodanie w³asnej grafiki w lewym panelu
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	c9319e32149026372a0d515ddbc1d14b
URL:		http://www.squirrelmail.org/plugin_view.php?id=30
Requires:	squirrelmail >= 1.4.6-2
Requires:	squirrelmail-compatibility-2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
This plugin allows the administrator to add a custom graphic to the
top of the left-hand pane of the main Mailbox view. The graphic will
be displayed immediately above the Folders list.

The graphic may be different for each domain you are hosting. See
config.php for more information and configuration instructions.

The plugin supports resizing the width of the left-hand pane by the
user.

%description -l pl
Wtyczka umo¿liwiaj±ca administratorowi dodanie w³asnej grafiki w lewym
panelu. Grafika bêdzie wy¶wietlana bezpo¶rednio nad list± folderów.

Mo¿na u¿yæ innej grafiki dla ka¿dej obs³ugiwanej domeny. Informacje i
szczególy dotycz±ce konfiguracji znajduj± siê w pliku config.php.

Wtyczka wspiera zmianê szeroko¶ci lewego panelu przez u¿ytkownika.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
cp config.php.typical.virtual.domain $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
